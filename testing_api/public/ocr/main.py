import cv2
import pytesseract
from pytesseract import Output

from flask import Flask, render_template, request, jsonify, json
import sys

app = Flask(__name__)

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def hello():
    print('hello')

@app.route('/api', methods=['GET'])

def index():
    # gambar = Getdata()
    img = cv2.imread('../images/Shoppe_pay.jpeg')

    image = img[175:220, 75:640]

    d = pytesseract.image_to_string(image)

    for b in d.splitlines():
        b = b.split(' ')

    d = b[0] + " " + b[1]

    if(d == "Transfer Bank" or d == "Transfer Antar"):

        image = img[250:850, 75:640]
        roi = [
            [(5, (11 + 23)), (82,640),'status'],
            [(66, (71 + 23)), (200,640),'nomor_transaksi'],
            [(95, (100 + 28)), (206,640),'tgl'],
            [(156, (161 + 23)), (155,640),'nomor_struk'],
            [(245, (250 + 28)), (108,640),'pengirim'],
            [(336, (341 + 23)), (150,640),'no_rekening_tujuan'],
            [(365, (370 + 24)), (179,640),'bank_penerima'],
            [(395, (400 + 24)), (120,640),'nama penerima'],
            [(455, (460 + 24)), (126,640),'jumlah']
        ]

        output = dict()

        for x,r in enumerate(roi):
            imgCrop = image[r[0][0]:r[0][1],r[1][0]:r[1][1]]

            text = pytesseract.image_to_string(imgCrop)
            
            if r[2] == 'status' :
                output['status'] = text.replace("\n","")
            if r[2] == 'nama penerima' :
                output['nama_penerima'] = text.replace("\n","")
            if r[2] == 'nomor_transaksi' :
                output['nomor_transaksi'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'nomor_struk' :
                output['nomor_struk'] = text.replace("\n","")
            if r[2] == 'pengirim' :
                output['pengirim'] = text.replace("\n","")
            if r[2] == 'no_rekening_tujuan' :
                output['no_rekening_tujuan'] = text.replace("\n","")
            if r[2] == 'bank_penerima' :
                output['bank_penerima'] = text.replace("\n","")
            if r[2] == 'nama_penerima' :
                output['nama_penerima'] = text.replace("\n","")
            if r[2] == 'jumlah' :
                output['jumlah'] = text.replace("\n","")

        return jsonify(output)

    elif(d == "Pembayaran/Pembelian ShopeePay"):

        image = img[250:850, 75:640]

        roi = [
            [(10,(16 + 28)),(90,640),'status'],
            [(79,(84 + 26)),(218 ,640),'no_transaksi'],
            [(113,(118 + 26)),(224,640),'tgl'],
            [(181,(186 + 26)),(170,640),'no_struk'],
            [(283,(288 + 26)),(168,640),'jns_pembelian'],
            [(317,(322 + 26)),(239,640),'no_hp'],
            [(385,(390 + 26)),(168,640),'reference'],
            [(419,(424 + 26)),(144,640),'nominal'],
            [(453,(458 + 26)),(160,640),'fee'],
            [(487,(492 + 26)),(220,640),'total']
        ]

        output = dict()

        for x,r in enumerate(roi):
            imgCrop = image[r[0][0]:r[0][1],r[1][0]:r[1][1]]

            text = pytesseract.image_to_string(imgCrop)

            if r[2] == 'status' :
                output['status'] = text.replace("\n","")
            if r[2] == 'no_transaksi' :
                output['no_transaksi'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'no_struk' :
                output['no_struk'] = text.replace("\n","")
            if r[2] == 'jns_pembelian' :
                output['jns_pembelian'] = text.replace("\n","")
            if r[2] == 'no_hp' :
                output['no_hp'] = text.replace("\n","")
            if r[2] == 'reference' :
                output['reference'] = text.replace("\n","")
            if r[2] == 'nominal' :
                output['nominal'] = text.replace("\n","")
            if r[2] == 'fee' :
                output['fee'] = text.replace("\n","")
            if r[2] == 'total' :
                output['total'] = text.replace("\n","")

        return jsonify(output)

    elif(d == "Pembayaran/Pembelian OVO"):

        image = img[250:850, 75:640]

        roi = [
            [(5, (11 + 23)), (82,640),'status'],
            [(66, (71 + 23)), (200,640),'nomor_transaksi'],
            [(95, (100 + 28)), (206,640),'tgl'],
            [(156, (161 + 23)), (155,640),'nomor_struk'],
            [(245, (250 + 28)), (150,640),'jenis_pembelian'],
            [(280,(285 + 23)),(210,640),'no_pelanggan'],
            [(310,(315 + 23)),(245,640),'nama_pelanggan'],
            [(336, (341 + 26)), (165,640),'nilai_topup'],
            [(395, (400 + 24)), (238,640),'total_bayar']
        ]

        output = dict()

        for x,r in enumerate(roi):
            imgCrop = image[r[0][0]:r[0][1],r[1][0]:r[1][1]]

            text = pytesseract.image_to_string(imgCrop)

            if r[2] == 'status' :
                output['status'] = text.replace("\n","")
            if r[2] == 'nomor_transaksi' :
                output['nomor_transaksi'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'nomor_struk' :
                output['nomor_struk'] = text.replace("\n","")
            if r[2] == 'jenis_pembelian' :
                output['jenis_pembelian'] = text.replace("\n","")
            if r[2] == 'no_pelanggan' :
                output['no_pelanggan'] = text.replace("\n","")
            if r[2] == 'nama_pelanggan' :
                output['nama_pelanggan'] = text.replace("\n","")
            if r[2] == 'nilai_topup' :
                output['nilai_topup'] = text.replace("\n","")
            if r[2] == 'total_bayar' :
                output['total_bayar'] = text.replace("\n","")

        return jsonify(output)

    elif(d == "Pembayaran/Pembelian Go"):

        image = img[250:850, 75:640]

        roi = [
            [(5, (11 + 23)), (82,640),'status'],
            [(66, (71 + 23)), (200,640),'nomor_transaksi'],
            [(95, (100 + 28)), (206,640),'tgl'],
            [(156, (161 + 23)), (155,640),'nomor_struk'],
            [(245, (250 + 28)), (180,640),'jenis_pembayaran'],
            [(280,(285 + 23)),(219,640),'no_handphone'],
            [(310,(315 + 23)),(230,640),'nama_costumer'],
            [(336, (341 + 23)), (150,640),'admin_fee'],
            [(365, (370 + 24)), (220,640),'nominal_topup'],
            [(395, (400 + 24)), (120,640),'no_reff'],
            [(427, (431 + 24)), (195,640),'total_bayar']
        ]

        output = dict()

        for x,r in enumerate(roi):
            imgCrop = image[r[0][0]:r[0][1],r[1][0]:r[1][1]]

            text = pytesseract.image_to_string(imgCrop)

            if r[2] == 'status' :
                output['status'] = text.replace("\n","")
            if r[2] == 'nomor_transaksi' :
                output['nomor_transaksi'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'nomor_struk' :
                output['nomor_struk'] = text.replace("\n","")
            if r[2] == 'jenis_pembayaran' :
                output['jenis_pembayaran'] = text.replace("\n","")
            if r[2] == 'no_handphone' :
                output['no_handphone'] = text.replace("\n","")
            if r[2] == 'nama_costumer' :
                output['nama_costumer'] = text.replace("\n","")
            if r[2] == 'admin_fee' :
                output['admin_fee'] = text.replace("\n","")
            if r[2] == 'nominal_topup' :
                output['nominal_topup'] = text.replace("\n","")
            if r[2] == 'no_reff' :
                output['no_reff'] = text.replace("\n","")
            if r[2] == 'total_bayar' :
                output['total_bayar'] = text.replace("\n","")

        return jsonify(output)

    elif(d == "Pembayaran/Pembelian DANA"):
        image = img[250:850, 75:640]

        roi = [
            [(6,(11 + 23)),(82,640),'status'],
            [(66,(71 + 23)),(201,640),'no_transaksi'],
            [(90,(100 + 28)),(204,640),'tgl'],
            [(155,(160 + 24)),(154,640),'no_struk'],
            [(246,(251 + 23)),(157,640),'jns_pembelian'],
            [(276,(281 + 23)),(90,640),'no_hp'],
            [(306,(311 + 23)),(243,640),'nama'],
            [(336,(341 + 25)),(170,640),'jumlah'],
            [(396,(401 + 23)),(0,640),'order_id'],
            [(425,(430 + 24)),(175,640),'transaksi_id'],
            [(456,(461+ 25)),(238,640),'total']

        ]

        output = dict()

        for x,r in enumerate(roi):
            imgCrop = image[r[0][0]:r[0][1],r[1][0]:r[1][1]]
            text = pytesseract.image_to_string(imgCrop)

            # cv2.imshow('img',imgCrop)
            cv2.waitKey(0)
            if r[2] == 'status' :
                output['status'] = text.replace("\n","")
            if r[2] == 'no_transaksi' :
                output['no_transaksi'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'tgl' :
                output['tgl'] = text.replace("\n","")
            if r[2] == 'no_struk' :
                output['no_struk'] = text.replace("\n","")
            if r[2] == 'jns_pembelian' :
                output['jns_pembelian'] = text.replace("\n","")
            if r[2] == 'no_hp' :
                output['no_hp'] = text.replace("\n","")
            if r[2] == 'nama' :
                output['nama'] = text.replace("\n","")
            if r[2] == 'jumlah' :
                output['jumlah'] = text.replace("\n","")
            if r[2] == 'order_id' :
                output['order_id'] = text.replace("\n","")
            if r[2] == 'transaksi_id' :
                output['transaksi_id'] = text.replace("\n","")
            if r[2] == 'total' :
                output['total'] = text.replace("\n","")

        return jsonify(output)

def Getdata():
    d = './images/Shoppe_pay.jpeg'
    return d

app.run()
