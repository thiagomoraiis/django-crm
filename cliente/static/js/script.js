quantidade = 0;

function less() {
    quantidade--;
    setValue(quantidade);
}

function more() {
    quantidade++;
    setValue(quantidade);
}

function setValue(value) {
    document.getElementById('num').value = value;
}

setValue(quantidade);
            