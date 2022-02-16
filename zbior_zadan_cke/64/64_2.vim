" wykonanie zadania 64.2 w vimscripcie
" aby wykonać należy otworzyć ten plik w edytorze vim i wpisać ':so %'
let plik = readfile("dane/dane_obrazki.txt")
let tile = []
let tile2 = []
let tile3 = []
let tile4 = []
let ilosc = 0
let licznik = 0
for i in range(len(plik))
	
	" Jeżeli nie jest to linia w której jest tabela
	if len(plik[i]) == 20 || len(plik[i]) == 0
		let tile = []
		let tile2 = []
		let tile3 = []
		let tile4 = []
		let licznik = 0
		continue
	endif

	let plik[i] = plik[i][:19]
	
	" Dzielenie na kafelki
	if licznik < 10
		call add(tile, plik[i][:9])
		call add(tile2, plik[i][10:])
		let licznik += 1
	elseif licznik >= 10
		call add(tile3, plik[i][:9])
		call add(tile4, plik[i][10:])
		let licznik += 1
	endif
	if tile == tile2 && tile2 == tile3 && tile3 == tile4
		let ilosc += 1
		if ilosc == 1
			echo "Linia: " .. i
		endif
	endif
endfor

echo ilosc
