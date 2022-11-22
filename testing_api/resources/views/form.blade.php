<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>
<body>
    <div class="card" style="margin: 10px 200px">
        <div class="card-header">d
            Featured
        </div>
        <div class="card-body">
            <form action="">
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Status</label>
                    <input type="text" class="form-control" id="status" placeholder="status" name="status" value="{{ $data['status'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Nomor Transaksi</label>
                    <input type="text" class="form-control" id="no_transaksi" placeholder="no_transaksi" name="no_transaksi" value="{{ $data['nomor_transaksi'] }}">
                </div>
                <div class="mb-3">
                    @php
                        $data['tgl'] = date('Y-m-d H:i', strtotime($data['tgl']))
                    @endphp
                    <label for="exampleFormControlInput1" class="form-label">Tanggal dan Waktu</label>
                    <input type="datetime-local" class="form-control" id="tgl" placeholder="tgl" name="tgl" value="{{ $data['tgl'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Nomor Struk</label>
                    <input type="text" class="form-control" id="no_struk" placeholder="no_struk" name="no_struk" value="{{ $data['nomor_struk'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Nama Pengirim</label>
                    <input type="text" class="form-control" id="pengirim" placeholder="pengirim" name="pengirim" value="{{ $data['pengirim'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Nomor Rekening Tujuan</label>
                    <input type="text" class="form-control" id="no_rekening_tujuan" placeholder="no_rekening_tujuan" name="no_rekening_tujuan" value="{{ $data['no_rekening_tujuan'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Bank Penerima</label>
                    <input type="text" class="form-control" id="bank_penerima" placeholder="bank_penerima" name="bank_penerima" value="{{ $data['bank_penerima'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Nama Penerima</label>
                    <input type="text" class="form-control" id="nama_penerima" placeholder="nama_penerima" name="nama_penerima" value="{{ $data['nama_penerima'] }}">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Admin Fee</label>
                    <input type="number" class="form-control" id="admin_fee" placeholder="admin_fee" name="admin_fee">
                </div>
                <div class="mb-3">
                    <label for="exampleFormControlInput1" class="form-label">Total</label>
                    <input type="number" class="form-control" id="total" placeholder="total" name="total" value="{{ $data['jumlah'] }}">
                </div>
            </form>
        </div>
    </div>


</body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous">
</script>

</html>
