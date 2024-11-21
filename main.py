'''
************************************************************************************
**
**    AUTHOR(S):
**     Leonel Nieto Lara
**
**    TITLE:
**      main.py
**
**    DESCRIPTION:
**      Script to transfer or upload files of flexmedia
************************************************************************************
'''
from ftplib import FTP
from tkinter import filedialog
import sys
import argparse

def parseArgs( sysargs ):
    parser = argparse.ArgumentParser( description="Duplicate the functionality of Filezila. " \
                                     + "Mandatory arguments: -i IPADDRESS, -u USER, -pw PASSWORD, -o Operation " \
                                         + "Optional args: -p PORT, -ph PATH, -f FILE" )
    parser.add_argument(
        '-i',
        '--ip',
        metavar='IPADDRESS',
        help='Flexmedia IP.',
        required=True
    )
    parser.add_argument(
        '-p',
        '--port',
        metavar='PORT',
        help='Protocol port: Default=21',
        required=False
    )
    parser.add_argument(
        '-u',
        '--username',
        metavar='USERNAME',
        help='Flexmedia Username.',
        required=True
    )
    parser.add_argument(
        '-pw',
        '--password',
        metavar='PASSWORD',
        help='Flexmedia password',
        required=True
    )
    parser.add_argument(
        '-o',
        '--operation',
        metavar='OPERATION',
        help='Operation to select, Download, Upload or List files',
        required=True
    )
    parser.add_argument(
        '-ph',
        '--path',
        metavar='PATH',
        help='Path file to upload to the Flexmedia or path of the file to download to your pc',
        required=False
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE',
        help='Name of the file you want to trasfer to your pc',
        required=False
    )
    args = parser.parse_args( sysargs )
    return args

class TransferFilesFTP( ):
    def __init__( self, ipAddres:str, username:str, password:str, port=21, ) -> None:
        self.IPADDRESS = ipAddres
        self.PORT      = port
        self.USERNAME  = username
        self.PASSWORD  = password

    def connectFTP( self ) -> None:
        try:
            self.ftp = FTP( self.IPADDRESS, self.USERNAME, self.PASSWORD, "host" )            
            self.ftp.connect(self.IPADDRESS, self.PORT )
            print( "The connection has been successfully established" )
        
        except:
            print( "The connection could not be established, check the data entered." )
            sys.exit( 1 )
    
    def uploadFiles( self, pathfile="" ) -> None:
        try:
            if pathfile == None:
                local_path = filedialog.askopenfilename( )
            else:
                local_path = pathfile

            index_last_slash = local_path.rfind( "/" ) + 1
            filename = local_path[ index_last_slash : len( local_path ) ]
            with open( local_path, 'rb' ) as file:
                self.ftp.storbinary( f'STOR { filename }', file )
                print( f"File: '{ filename }' upload successfully" )

        except Exception as e:
            print( f"Fail to upload the file: {e}" )
            sys.exit( 1 )
    
    def downloadFiles( self, file_name:str ) -> None:
        try:
            local_path =  file_name
            with open( local_path, 'wb' ) as file:
                self.ftp.retrbinary( f'RETR {file_name}', file.write )
                print( f"File '{file_name}' downloaded successful to '{ local_path }'" )
        
        except Exception as e:
            print( f"-- FAIL TO DOWNLOAD THE FILE -- \n {e}" )
            sys.exit( 1 )

    def list_files( self, directory = "/" ) -> None:
        self.ftp.cwd( directory )
        self.ftp.retrlines( 'LIST' )

    def disconnect( self ) -> None:
        if self.ftp:
            self.ftp.quit( )
            print( "Connection closed" )
        
        else:
            print( "There isn't any connection to close" )

if __name__ == "__main__":
    args      = parseArgs( sys.argv[ 1 : ] )
    IPADDRESS = args.ip
    PORT      = args.port
    USERNAME  = args.username
    PASSWORD  = args.password
    PATH      = args.path
    FILENAME  = args.file
    OPERATION = args.operation

    transferfilesFTP = TransferFilesFTP( IPADDRESS, USERNAME, PASSWORD )
    transferfilesFTP.connectFTP( )
    if OPERATION == "List":
        transferfilesFTP.list_files( )
    elif OPERATION == "Upload":  
        transferfilesFTP.uploadFiles( PATH )
    elif OPERATION == "Download":
        transferfilesFTP.downloadFiles( FILENAME )
    transferfilesFTP.disconnect( )
