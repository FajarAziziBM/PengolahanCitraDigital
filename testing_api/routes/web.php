<?php

use GuzzleHttp\Client;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/api-get-data', function(){
    $client = new Client();
    $response = $client->request('GET','http://127.0.0.1:5000/api');
    $status_code = $response->getStatusCode();
    $body = $response->getBody()->getContents();
    $data = json_decode($body, true);
    return view('form', [
        'data' => $data
    ]);
});
