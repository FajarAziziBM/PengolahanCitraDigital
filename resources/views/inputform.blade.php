@extends('layout.main')
@section('container')
    <!-- Content wrapper -->
    <div class="content-wrapper">
        <div class="container-xxl flex-grow-1 container-p-y">
            <div class="row">
                <div class="col">
                    <h1 class="fw-bold fs-2 mb-5"></h1>
                </div>
            </div>

            <!-- Content -->
            <main>
                <div class="row">
                    <div class="col col-md-9">
                        <a class="btn btn-outline-secondary" href="">
                            <i class="fa-regular fa-chevron-left me-2"></i>
                            Kembali
                        </a>

                        <div class="card mt-3">
                            <div class="card-body">
                                <form action="" method="post" enctype="multipart/form-data">
                                    @csrf
                                    <div class="mb-3">
                                        <label for="thumbnail" class="form-label">Thumbnail</label>
                                        <img class="img-preview img-fluid mb-3 col-sm-5">
                                        <input class="form-control" type="file" name="thumbnail" id="thumbnail"
                                            onchange="previewImage()">
                                        <div id="thumbnailHelp" class="form-text">Ekstensi file: JPG, PNG maksimal 2MB</div>
                                    </div>

                                    <div class="text-end">
                                        <button type="submit" class="btn btn-primary">Buat Berita</button>
                                    </div>

                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function previewImage() {
                        const image = document.querySelector('#thumbnail');
                        const imgPreview = document.querySelector('.img-preview');
                        imgPreview.style.display = 'block';
                        const oFReader = new FileReader();
                        oFReader.readAsDataURL(image.files[0]);
                        oFReader.onload = function(OFREvent) {
                            let data = OFREvent.target.result;
                            $.ajax({
                                url: "http://127.0.0.1:5000/getdata",
                                type: "POST",
                                data: JSON.stringify({
                                    'gambar': data
                                }),
                                dataType: 'json',
                                headers: {
                                    'X-CSRF-TOKEN': '{{ csrf_token() }}',
                                    'Content-Type': 'application/json'
                                },
                                success: function(result) {
                                    console.log(result)
                                }
                            });
                        }
                    }
                </script>

                <script type="text/javascript" src="{{ asset('js/trix.js') }}"></script>
            </main>
        </div>
        <!-- / Content -->
        <div class="content-backdrop fade"></div>
    </div>
    <!-- / Content wrapper -->
@endsection
