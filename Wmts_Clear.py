import os, os.path
from datetime import datetime
#---------------------------------------------------------------------------------------------------#
zoom=11 #seçilen seviye ve yukarısı temizlenecektir.
Klasor="C:\\Users\\burak\\Desktop\\BOTAS\\WMTS\\ayvalik_20_jpeg"
#---------------------------------------------------------------------------------------------------#
start_time = datetime.now()
deleted=0
filesize=0
for zoom in range(zoom,21):
    zoom=zoom+1
    Dizin=(Klasor+"\\"+ str(zoom))
    print(Dizin, "directory cleared.")
  
    for root, _, files in os.walk(Dizin):        
        for f in files:
            fullpath = os.path.join(root, f)            
            try:
                if os.path.getsize(fullpath) < 3723:   # byte 1652 for jpeg_19,  5169 for png_19, 3723 for jpeg_20
                    deleted=deleted+1
                    filesize=filesize+os.path.getsize(fullpath)                    
                    os.remove(fullpath)            

            except WindowsError:
                print( "Error" + fullpath)
            
end_time = datetime.now()
print("Total Deleted File Count= " ,deleted," Files")
print("Total Deleted File Size= " ,round((filesize/(1024*1024)),2) ," Megabyte")
print('Duration: {}'.format(end_time - start_time))


