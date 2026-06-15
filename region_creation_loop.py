##### Script that creates regions with names from A -Z

import random

def make_region():
    
    # clear the previous output
    RPR_ClearConsole()
    
    # get total number of regions
    total = RPR_GetNumRegionsOrMarkers(0)
    
    # NAME LIST LOOP
    
    # makes list of region names
    names=[]
    
    for i in range(total):
        # Get region details
        reg_specs=RPR_EnumProjectMarkers2(0, i, True, 0, 0, "" , 0)
        
        # Get just the index value
        index=reg_specs[2]
        
        # Convert index to a pointer in Reaper
        pointer=RPR_GetRegionOrMarker(0, index, "")
        
        # Get the name of region
        reg_info=RPR_GetSetRegionOrMarkerInfo_String(0, pointer, "P_NAME", "", False)
        name=reg_info[4]
        
        # Add name to a list
        names.append(name)
        
     # Display list of names
    RPR_ShowConsoleMsg(f"{names}\n")
        
        
  # NAME CREATION PORTION
        
  # List of posible region names (A - Z)
    alphabet="ABCDEFGHIJKLMNOPQRSTUVXYZ"
    reg_name="A"
        
  # Loops through alphabet to get name 
    for letter in alphabet:
      if letter not in names:
        reg_name=letter
        break
  
  # random color generator
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    
  # Reaper color format conversion
    color= RPR_ColorToNative(r,g,b)| 0x1000000
        
  # CREATE REGION
  
  # get time data
    time_data=RPR_GetSet_LoopTimeRange(False, False, 0, 0, False)
    start=time_data[2]
    end=time_data[3]
          
  # ERROR: No time selected
    if start==end:
      RPR_ShowConsoleMsg("ERROR: Time selection missing\n")
      return
         
    RPR_AddProjectMarker2(0,True, start, end, reg_name, 0, color)
    
if __name__ == "__main__":
  make_region()

