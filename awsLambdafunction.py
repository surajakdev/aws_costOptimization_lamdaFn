import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all the ebs snapshots
    response = ec2.describe_snapshots(
       OwnerIds = ['self']
    )

    # Get all active ec2 instance ids
    instance_response = ec2.describe_instances(filters=[{'Name':'instance-state-name','values': ['running']}])
    active_instance_ids = set()

    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if its not attached to any volume or
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # delete the snapshot it its not attached to volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"deleted ebs snapshot {snapshot_id} as it was not attached to any volume")

        else:
            # check if volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(Snapshot_Id=snapshot_id)
                    print(f"Deleted ebs snapshot {snapshot_id} as it was taken from a volume not attached to ec2 instance")
            except ec2.exceptions.ClientError as e :
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found ( it might)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted ebs snapshot {snapshot_id} as its associated volume was not found.")
