import os, os.path
from datetime import datetime

def toplam_boyut(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += toplam_boyut(entry.path)
    return total

def clearTiles(): 
    #-----------------------------------------Data Girişi--------------------------------------------------------------------------#

    zoom=11 #seçilen seviye ve yukarısı temizlenecektir.
    Klasor="C:\\Users\\burak\\Desktop\\BOTAS\\WMTS\\ayvalik_20_jpeg2" #temizlenecek dizin.
    minSize=1711 # byte - silinecek dosya boyutu-  1711 for jpeg_19,  5169 for png_19.
    #-------------------------------------------------------------------------------------------------------------------------------#

    start_time = datetime.now()
    deleted_count=0
    deleted_size=0
    total_files = sum(len(files) for _, _, files in os.walk(Klasor))
    total_size = round(toplam_boyut(Klasor)/(1024*1024),2)

    for zoom in range(zoom,21):
        zoom=zoom+1
        Dizin=(Klasor+"\\"+ str(zoom))

        for root, _, files in os.walk(Dizin):        
            for f in files:
                dosyayolu = os.path.join(root, f)            
                try:
                    if os.path.getsize(dosyayolu) < minSize:   
                        deleted_count=deleted_count+1
                        deleted_size=deleted_size+os.path.getsize(dosyayolu)                    
                        os.remove(dosyayolu)            

                except WindowsError:
                    print( "Error" + dosyayolu)
        print(Dizin, "directory cleared.") 

    end_time = datetime.now()
    duration='Duration: {}'.format(end_time - start_time)
    after_files=sum(len(files) for _, _, files in os.walk(Klasor))
    after_size=round(toplam_boyut(Klasor)/(1024*1024),2)
    dizin_report=os.path.basename(os.path.normpath(Klasor)) 
    
    if deleted_count!=0:
        if not os.path.isfile("C:\Wmts_Clear_Report.txt"):
            f = open("C:\Wmts_Clear_Report.txt", "a+")
            f.write("      "+"Tarih"+"               "+"Dizin"+"        "+"Toplam Dosya"+"    "+"Toplam Veri"+"       "+"Silinen Dosya"+"     "+"Silinen Veri"+"     "+"Kalan Dosya"+"    "+"Kalan Veri"+"    "+"Reduction"+"          "+"hh:mm:ss"+"\n")
            f.write((datetime.strftime((datetime.now()), '%x'))+"-"+(datetime.strftime((datetime.now()), '%X'))+"    "+str(dizin_report)+"      "+ str(total_files)+"        "+ str(total_size)+" mb"+"            "+str(deleted_count)+"          "+str(round((deleted_size/(1024*1024)),2)) + " mb"+"           "+ str(after_files)+"          "+str(after_size)+" mb"+"      "+str(('{:.1%}'.format((deleted_size/(1024*1024))/total_size)))+"       "+str(duration)+"\n")
            f.close()
        else:
            f = open("C:\Wmts_Clear_Report.txt", "a+")
            f.write((datetime.strftime((datetime.now()), '%x'))+"-"+(datetime.strftime((datetime.now()), '%X'))+"    "+str(dizin_report)+"      "+ str(total_files)+"        "+ str(total_size)+" mb"+"            "+str(deleted_count)+"          "+str(round((deleted_size/(1024*1024)),2)) + " mb"+"           "+ str(after_files)+"          "+str(after_size)+" mb"+"      "+str(('{:.1%}'.format((deleted_size/(1024*1024))/total_size)))+"       "+str(duration)+"\n")
            f.close()

    print("New Data Size: ",after_size)
    print("Total Reduction :",('{:.1%}'.format((deleted_size/(1024*1024))/total_size)))
    print("Check Report File for Details: C:\Wmts_Clear_Report.txt")

clearTiles()