#Function untuk validasi password
def password_check(passwd):

    SpecialSym =['$', '!', '@', '#', '%', '^', '&', '*', '_', '-', '(', ')']
    val=True

    if len(passwd) < 8:
        print('Password harus berisi 8 karakter')
        val=False

    if len(passwd) > 8:
        print('Password harus berisi 8 karakter')
        val=False

    if not any(char.isdigit() for char in passwd):
        print('Password harus berisi minamal satu angka')
        val=False

    if not any(char.isupper() for char in passwd):
        print('Password harus berisi minimal satu huruf besar')
        val=False

    if not any(char.islower() for char in passwd):
        print('Password harus berisi minimal satu huruf kecil')
        val=False

    if not any(char in SpecialSym for char in passwd):
        print('Password harus berisi minimal satu karakter spesial (!@#$%^&*-_)')
        val=False

    if val:
        return val

#Main Method
def main():
    passwd = input('Masukkan password: ')
    print('\n')

    if (password_check(passwd)):
        print('Password valid')
    else:
        print('Password tidak valid')
        #return main() | Jika ingin mengulang program jika password tidak valid

#Driver Code
if __name__ == '__main__' :
    main()