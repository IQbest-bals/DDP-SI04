{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOX+uQcjwb0HIjiMYh2rZ7I"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["#arithmetic operator\n","\n","a = 13\n","b = 3\n","\n","hasil = a % b\n","\n","print(hasil)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"NsMr2oYfYQd3","executionInfo":{"status":"ok","timestamp":1729150979643,"user_tz":-420,"elapsed":560,"user":{"displayName":"Iqbal Hermawan","userId":"09399263066952976130"}},"outputId":"1c32bd21-da2b-4863-b4f6-74b9dddf935f"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["1\n"]}]},{"cell_type":"markdown","source":[],"metadata":{"id":"Q15U2eirbjCN"}},{"cell_type":"markdown","source":["TB = int(input('masukan tinggi badan'))\n","bb_ideal = (TB - 100) - (TB - 100) * 0,1\n","\n","print(\"berat badan ideal adalah :\",bb_ideal)"],"metadata":{"id":"33pBLQgsjMam"}},{"cell_type":"code","source":["nilaiujian = int(input(\"masukkan nilai ujian\"))\n","Lulus = \"kamu berhasil\"\n","Tidaklulus = \"coba lagi\"\n","\n","if nilaiujian >= 75:\n"," print(\"Lulus\")\n","else:\n"," print(\"Tidak lulus\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"28lN0iYXfqh9","executionInfo":{"status":"ok","timestamp":1729308963074,"user_tz":-420,"elapsed":9707,"user":{"displayName":"Iqbal Hermawan","userId":"09399263066952976130"}},"outputId":"184a78a4-ad2d-401b-b16e-f8c035724c5c"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["masukkan nilai ujian85\n","Lulus\n"]}]},{"cell_type":"code","source":["angka = int (input (\"masukkan bilangan bulat: \"))\n","ganjil = \"bilangan ganjil\"\n","genap = \"bilangan genap\"\n","\n","if angka % 2 == 0:\n"," print(\"Genap\")\n","elif (angka % 2 != 0):\n"," print(\"Ganjil\")\n","else:\n"," print(\"input tidak valid\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"9gMf4WzDbn4f","executionInfo":{"status":"ok","timestamp":1729154897715,"user_tz":-420,"elapsed":18962,"user":{"displayName":"Iqbal Hermawan","userId":"09399263066952976130"}},"outputId":"15834561-1780-40b9-8497-4f1c531f0b4d"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["masukkan bilangan bulat: 67\n","Ganjil\n"]}]},{"cell_type":"code","source":["status = (input(\"masukkan status voucher anda\"))\n","\n","if status == \"gold\" or status == \"platinum\":\n"," print(\"Angzay dapet diskon 75%\")\n","else:\n"," print(\"yaaa kasian\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"VBkX9QdMk9rq","executionInfo":{"status":"ok","timestamp":1729157215730,"user_tz":-420,"elapsed":3974,"user":{"displayName":"Iqbal Hermawan","userId":"09399263066952976130"}},"outputId":"d5d85adf-e269-4e1d-a1cc-4898cb077748"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["masukkan status voucher andagold\n","Angzay dapet diskon 75%\n"]}]},{"cell_type":"code","source":["Pembelian = int(input(\"Masukkan harga total belanja anda\"))\n","hargabarang = 8000\n","\n","if Pembelian > 100:\n"," print(Pembelian * 10/100)\n","else:\n"," print(Pembelian)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"0oKTLXXRvOeg","executionInfo":{"status":"ok","timestamp":1729156817338,"user_tz":-420,"elapsed":6499,"user":{"displayName":"Iqbal Hermawan","userId":"09399263066952976130"}},"outputId":"3af6bd6f-741e-4413-9d5a-2a94b4e8183d"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Masukkan harga total belanja anda60000\n","6000.0\n"]}]}]}