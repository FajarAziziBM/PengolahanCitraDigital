<?php

namespace Database\Seeders;

// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // \App\Models\User::factory(10)->create();

        // \App\Models\User::factory()->create([
        //     'name' => 'Test User',
        //     'email' => 'test@example.com',
        // ]);
        \App\Models\User::create([
            'name' => 'Administrator',
            'username' => 'admin',
            'email' => 'admin@gmail.com',
            'no_rekening' => '0987654321',
            'is_active' => 'aktif',
            'is_admin' => '1',
            'password' => Hash::make('admin')
        ]);
        \App\Models\User::create([
            'name' => 'Karyawan',
            'username' => 'tes',
            'email' => 'tes@gmail.com',
            'no_rekening' => '0987654321',
            'is_active' => 'aktif',
            'is_admin' => '0',
            'password' => Hash::make('123')
        ]);
    }
}
