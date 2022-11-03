function formataMoeda(el, SeparadorMilesimo, SeparadorDecimal, e) {
	const objTextBox = el;
	const maxLen = objTextBox.getAttribute('maxlength');
	let len = objTextBox.value.length;
	let key = '';
	let i = 0;
	const strCheck = '0123456789';
	let aux = '';
	const whichCode = (window.addEventListener) ? e.which : e.keyCode;
	// 13=enter, 8=backspace as demais retornam 0(zero)
	// whichCode==0 faz com que seja possivel usar todas as teclas como delete, setas, etc
	if ((whichCode === 13) || (whichCode === 0) || (whichCode === 8)) {
		return true;
	}
	key = String.fromCharCode(whichCode); // Valor para o código da Chave


	if (strCheck.indexOf(key) === -1) {
		return false;
	} // Chave inválida

	if (len >= maxLen) {
		return false;
	}

	for (i = 0; i < len; i += 1) {
		if ((objTextBox.value.charAt(i) !== '0') && (objTextBox.value.charAt(i) !== SeparadorDecimal)) {
			break;
		}
	}
	for (; i < len; i += 1) {
		if (strCheck.indexOf(objTextBox.value.charAt(i)) !== -1) {
			aux += objTextBox.value.charAt(i);
		}
	}
	aux += key;
	len = aux.length;
	if (len === 0) {
		objTextBox.value = '';
	}
	if (len === 1) {
		objTextBox.value = `0${SeparadorDecimal}0${aux}`;
	}
	if (len === 2) {
		objTextBox.value = `0${SeparadorDecimal}${aux}`;
	}
	if (len > 2) {
		let aux2 = '';
		let len2 = 0;
		let j = 0;
		for (j = 0, i = len - 3; i >= 0; i -= 1) {
			if (j === 3) {
				aux2 += SeparadorMilesimo;
				j = 0;
			}
			aux2 += aux.charAt(i);
			j += 1;
		}
		objTextBox.value = '';
		len2 = aux2.length;
		for (i = len2 - 1; i >= 0; i -= 1) {
			objTextBox.value += aux2.charAt(i);
		}
		objTextBox.value += SeparadorDecimal + aux.substr(len - 2, len);
	}
	return false;
}
const elem = document.getElementById('money-mask');
elem.onkeypress = e => formataMoeda(e.target, '.', ',', e);


function MascaraMoeda(objTextBox, SeparadorMilesimo, SeparadorDecimal, e){
    var sep = 0;
    var key = '';
    var i = j = 0;
    var len = len2 = 0;
    var strCheck = '0123456789';
    var aux = aux2 = '';
    var whichCode = (window.Event) ? e.which : e.keyCode;
    if (whichCode == 13) return true;
    key = String.fromCharCode(whichCode); // Valor para o c�digo da Chave
    if (strCheck.indexOf(key) == -1) return false; // Chave inv�lida
    len = objTextBox.value.length;
    for(i = 0; i < len; i++)
        if ((objTextBox.value.charAt(i) != '0') && (objTextBox.value.charAt(i) != SeparadorDecimal)) break;
    aux = '';
    for(; i < len; i++)
        if (strCheck.indexOf(objTextBox.value.charAt(i))!=-1) aux += objTextBox.value.charAt(i);
    aux += key;
    len = aux.length;
    if (len == 0) objTextBox.value = 'R$ ';
    if (len == 1) objTextBox.value = 'R$ '+ SeparadorDecimal + aux;
    if (len == 2) objTextBox.value = 'R$ '+ SeparadorDecimal + aux;
    if (len > 2) {
        aux2 = '';
        for (j = 0, i = len - 3; i >= 0; i--) {
            if (j == 3) {
                aux2 += SeparadorMilesimo;
                j = 0;
            }
            aux2 += aux.charAt(i);
            j++;
        }
        objTextBox.value = 'R$ ';
        len2 = aux2.length;
        console.log(aux2);
        for (i = len2 - 1; i >= 0; i--)
        objTextBox.value += aux2.charAt(i);
        objTextBox.value += SeparadorDecimal + aux.substr(len - 2, len);
    }
    return false;
}