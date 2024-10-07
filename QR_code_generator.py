import qrcode
import os.path


def generate_qr(data, file_name, fill_color='black', back_color='white'):
    def save_file(file_name):
        name, number = file_name, 0
        while os.path.isfile(name + '.png'):
            number += 1
            name = f"{str(name)}_{str(number)}"
        image.save(name + '.png')
        return name + '.png'

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color=fill_color, back_color=back_color)
    print(f'QR code saved as {save_file(file_name)}')

datas = input('Enter text or URLs separated by spaces: ').strip().split(' ')
file_name = input('Enter the filename for each data: ').strip().split(' ')

file_name[0] = 'qr_code' if file_name[0] == '' else file_name[0]

for data in range(0, len(datas)):
    generate_qr(datas[data], file_name[data]) if len(file_name) > data else generate_qr(datas[data], f'qr_code{data}')
