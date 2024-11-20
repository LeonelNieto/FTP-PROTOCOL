from ftplib import FTP
from tkinter import filedialog
import sys

IPADDRESS  = sys.argv[ 1 ]
USERNAME   = sys.argv[ 2 ]
PASSWORD   = sys.argv[ 3 ]
OPERATION  = sys.argv[ 4 ]
SCRIPTNAME = sys.argv[ 5 ] 

class TransferFilesFTP( ):
    def __init__( self, ipAddres:str, username:str, password:str, port=21 ) -> None:
        self.IPADDRESS = ipAddres
        self.USERNAME  = username
        self.PASSWORD  = password
        self.PORT      = port

    def connectFTP( self ):
        try:
            self.ftp = FTP( self.IPADDRESS, self.USERNAME, self.PASSWORD, "host" )            
            self.ftp.connect(self.IPADDRESS, self.PORT )
            print( "--- SUCCESSFUL CONNECTION ---" )
        
        except:
            print( "No se ha podido establecer la conexión, revisa los datos ingresados" )
            sys.exit( 1 )
    
    def uploadFiles( self ):
        try:
            local_path = filedialog.askopenfilename( )
            index_last_slash = local_path.rfind( "/" ) + 1
            filename = local_path[ index_last_slash : len( local_path ) ]
            print(filename)
            with open( local_path, 'rb' ) as file:
                self.ftp.storbinary( f'STOR {filename}', file )
                print( f"File: '{filename}' upload successfully" )

        except Exception as e:
            print( f"Fail to upload the file: {e}" )
            sys.exit( 1 )
    
    def downloadFiles( self, file_name:str):
        try:
            local_path =  file_name
            with open(local_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {file_name}', file.write)
                print(f"Archivo '{file_name}' descargado exitosamente a '{local_path}'")
        
        except Exception as e:
            print(f"Error al descargar el archivo: {e}")
            sys.exit( 1 )

    def list_files( self, directory = "/" ):
        self.ftp.cwd( directory )
        self.ftp.retrlines( 'LIST' )

    def disconnect( self ):
        if self.ftp:
            self.ftp.quit( )
            print( "Connection closed" )
        
        else:
            print( "There isn't any connection to close" )

if __name__ == "__main__":
    transferfilesFTP = TransferFilesFTP( IPADDRESS, USERNAME, PASSWORD )
    transferfilesFTP.connectFTP( )
    if OPERATION == "List":
        transferfilesFTP.list_files( )
    elif OPERATION == "Upload":  
        transferfilesFTP.uploadFiles( )
    elif OPERATION == "Download":
        transferfilesFTP.downloadFiles( "Archivo.txt" )
    transferfilesFTP.disconnect( )
