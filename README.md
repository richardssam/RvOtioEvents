# RvOtioEvents

Currently this is a plugin for RV which logs what media is being viewed at what time.
Down the road we could have it record other events so that we could play back the events and re-create a session. We are deliberatey using a neutral format, using OTIO as a serializer, so that similar plugins could be written for other playback tools.

The hope is that this is also useful for machine learning to identify what the viewer is looking at.

This is highly inspired by the work being done by the ASWF ORI team for review sync - See - https://lf-aswf.atlassian.net/wiki/spaces/PRWG/pages/11274625/OTIO-Based+Synchronized+Review+Messaging .

One notable change however, is that we are using https://jsonlines.org/ formatting, so that each line is a separate event. This makes it easy to write out events as they are coming in, and not expect the whole file to be a legal json structure. 

## Example log file
See [Log file](examples/otio_events_20250623_125823.jsonl)

## Installing
Download the [otioevents.zip](https://github.com/richardssam/RvOtioEvents/raw/refs/heads/main/otioevents.zip) file and install it with the OpenRV/RV  using the packages dialog under preferences.

## Building the package
THe script
```
makepackage.csh
```

## Extracting the data for ML.

The script `testdecode.py` is an example of how the file could be decoded, and additional metadata extracted from the file-path before ingest into a LLM.


