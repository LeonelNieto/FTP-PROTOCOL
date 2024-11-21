# Upload and Download files to Flexmedia
This proyect has the intention to replace filezila app, automate some tests or integrate it to a new tool. 

## REQUIREMENTS
You can use main.exe or source code, if you use executable app, you don't need to install anything, just excetute the app from the cmd with the requiered args.
If you want to use the source code, you only need to install python.

## HOW TO USE IT
You shall use the mandatory args, and you should use the optional args, according at your application.

**Mandatory args**

|         Command         |           Description           |             Example             |
|-------------------------|---------------------------------|---------------------------------|
|**-i** or **--ip**       | Flexmedia IP address            | -i 192.168.0.110                |
|**-u** or **username**   | Flexmedia username              | -u root                         |
|**-pw** or **--password**| Flexmedia password              | -pw password                    |
|**-o** or **--operation**| Download, Upload or List files  | -o Download, -o Upload, -o List |

Using **main.exe**: *main.exe -i 192.168.0.110 -u root -pw password -o Download -f script.sh*
Using **main.py**: *python main.py -i 192.168.0.110 -u root -pw password -o List*

> [!IMPORTANT]
> Take care, if you use -o Download option you shall user -f *File_to_download_name*

**Optional args**

|         Command         |             Description             |             Example             |
|-------------------------|-------------------------------------|---------------------------------|
|**-p** or **--port**     | Port, default = 21                  | -p 22                           |
|**-ph** or **path**      | Path file to upload or download     | -ph C:\Downloads                |
|**-f** or **--file**     | Name file to download from flexmedia| -f script.sh                    |

> [!IMPORTANT]
> If you don't add the -ph option, will pop up a window asking for a directory **Only in Upload option**