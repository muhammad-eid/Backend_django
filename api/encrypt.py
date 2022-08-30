from cryptography.fernet import Fernet
import json



key = b'PBM-nz2qLOddOjThsBK1T1Ymvmcl46kjUhLh_LVD2AE='
key_ = b'yQ1ajTspiE0zHBJSDbKl4xPdlpYzM87VY-G5jdY-Pf0='
fernet = Fernet(key)
fernet_ = Fernet(key_)



#server
def encrypt(data:dict):
    return fernet.encrypt(str(data).encode())

def decrypt(data:str):
    decMessage = fernet_.decrypt(data).decode().replace("\'", "\"")
    return json.loads(decMessage)


#client
def encrypt_(data:dict):
    return fernet_.encrypt(str(data).encode())


def decrypt_(data:str):
    decMessage = fernet.decrypt(data).decode().replace("\'", "\"")
    return json.loads(decMessage)

##############################################################################
##############################################################################
##############################################################################





# def test_enc(message = "hello geeks"):
#     encMessage = fernet.encrypt(message.encode())
#     decMessage = fernet.decrypt(encMessage).decode()
#     print("original string: ", message)
#     print("encrypted string: ", encMessage)
#     print("decrypted string: ", decMessage)


# # test_rsa()
# # test_enc()




# def test_client_to_server(message = {'a':1, 'b':2}):
#     enc_data = encrypt_(message)
#     dec_data = decrypt(enc_data)

#     print(enc_data)
#     print(dec_data)
#     print(type(enc_data))
#     print(type(dec_data))

# def test_server_to_cleint(message = {'c':3, 'd':4}):
#     enc_data =  encrypt(message)
#     dec_data = decrypt_(enc_data)
#     print(enc_data)
#     print(dec_data)
#     print(type(enc_data))
#     print(type(dec_data))


# # test_client_to_server()
# # test_server_to_cleint()


# data = {
#     'key': 'key',
#     'type': 'type',
#     'duration': 'duration',
#     'user_name': 'user_name',
#     'uuid': 'uuid',
#     'hddid': 'hddid',
#     'mac_address': 'mac_address',
#     'os_version': 'os_version',
#     'sw_version': 'sw_version',
# }


# print(encrypt_(data))
# print(decrypt(encrypt_(data)))

