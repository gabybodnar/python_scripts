### Script to add template track with desired attributes
#### (for my volca bass synth)

RPR_ClearConsole()

# disarm record button on already existing tracks in 
# project to record only on th newly created track

def disarm_record():
  # Count the tracks
  track_count=RPR_CountTracks(0)
  # disarming loop 
  for track in range(track_count):
    # get the pointer of the track
    pointer=RPR_GetTrack(0,track)
    # disarm record button
    RPR_SetTrackUIRecArm(pointer,0,0)


def insert_track():
  
  # Count Tracks
  track_count=RPR_CountTracks(0)
  
  # Add track
  RPR_InsertTrackAtIndex(track_count, True)
  
  # Gets us pointer of track
  pointer=RPR_GetTrack(0,track_count)
  
  # Name the track
  RPR_GetSetMediaTrackInfo_String(pointer, "P_NAME", "volca_bass", True)
  
  #Color Variable
  blue=RPR_ColorToNative(0,49,81)|0x1000000
  
  # Color the track
  RPR_SetTrackColor(pointer, blue)
  
  # Set input source 
  RPR_SetMediaTrackInfo_Value(pointer, "I_RECINPUT", 1)
  # Turn on Input Monitoring
  RPR_SetTrackUIInputMonitor(pointer,1,0)
  
  # Turn on recording
  RPR_SetTrackUIRecArm(pointer,1,0)
  
  # Add input plugin
  input_plugin="VST3:mvMeter2"
  
  RPR_TrackFX_AddByName(pointer,input_plugin,True,-1)
  
  # Add output plugins
  plugin_chain=["VST3:mvMeter2" , "JS: Loudness Meter Peak/RMS/LUFS (Cockos)"]
  
  for plugin in plugin_chain:
    RPR_TrackFX_AddByName(pointer,plugin,False,-1)
  
disarm_record()

insert_track()


