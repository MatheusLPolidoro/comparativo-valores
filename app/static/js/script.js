function validateForm() {
    var query = document.forms["searchForm"]["query"].value;
    var quantity = document.forms["searchForm"]["quantity"].value;

    if (query.trim() === "") {
        alert("Por favor, digite o item que seja buscar!");
        return false;
    }

    if (quantity.trim() === "" || isNaN(quantity) || quantity < 10 || quantity > 100) {
        alert("Por favor, digite uma quantidade de itens entre 10 e 100!");
        return false;
    }
}