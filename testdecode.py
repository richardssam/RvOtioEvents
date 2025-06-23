import json

import os
import sys

# This script decodes a JSONL file containing OTIO events and extracts metadata from the file paths.
# It assumes the file paths follow a specific structure and extracts project, sequence, shot, and task information from them.
# The script reads the file paths from the 'mediaReference' field in each event, decodes them, and outputs the results as a JSON array.

filename = sys.argv[1] if len(sys.argv) > 1 else "examples/otio_events_20250623_125823.jsonl"
decodeddata = []
with open(filename, "r") as f:
    for line in f:
        # This really should be replaced by the OTIO schema parser, but for now we will just use json.loads
        event = json.loads(line)
        filepath = event['mediaReference']['target_url']
        # Now we do a really crude decode of the filepath to get some metadata from the path, this would be substituted with a proper parser based on your project structure
        args = filepath.split('/')
        project = args[2]
        sequence = args[3]
        shot = args[4]
        task = args[5]
        decodeddata.append({'project': project, 'sequence': sequence, 'shot': shot, 'task': task, 'filepath': filepath, 'starttime': event['timestamp']})

# Write out decoded data as JSON
print(json.dumps(decodeddata, indent=4))
