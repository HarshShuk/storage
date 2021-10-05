import dropbox 
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token='pgw_vWqnIBYAAAAAAAAAARRkJs1aMTZLKX9mWe9uNVp1fRCLdE8hqPU31eSzCkaO'
    transferData=TransferData(access_token)
    file_from=input("Enter Path To Transfer Data:")
    file_to=input("Enter Full Path To Upload To Dropbox:")
    transferData.upload_file(file_from,file_to)
    print("File Has Been Moved")
main()