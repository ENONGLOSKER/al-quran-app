from django.shortcuts import render
import requests

# Create your views here.
def alquran_list(request):
    # surah_number = request.GET.get('surah', 1)
    api_url = f"https://quran-api.santrikoding.com/api/surah"

    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        return render(request, 'index.html', {'data': data})
    else:
        return render(request, 'index.html', {'data': None})
def alquran_details(request, id):
    if not id:
        return render(request, 'error.html', {'error_message': 'ID is required'})

    api_url = f"https://quran-api.santrikoding.com/api/surah/{id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # Extract `ayat` and other relevant data
        ayat = data.get('ayat', [])
        surah_info = {
            'nama': data.get('nama', ''),
            'nama_latin': data.get('nama_latin', ''),
            'jumlah_ayat': data.get('jumlah_ayat', 0),
            'tempat_turun': data.get('tempat_turun', ''),
            'arti': data.get('arti', ''),
            'audio': data.get('audio', ''),
        }
        return render(request, 'details.html', {'surah_info': surah_info, 'ayat': ayat})
    else:
        return render(request, 'error.html', {'error_message': 'Failed to retrieve data'})
