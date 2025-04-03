function searchItems() {
    if (event) event.preventDefault();

    const query = document.getElementById("search-input").value.trim();
    const resultsList = document.getElementById("results");

    resultsList.innerHTML = "";

    if (!query) {
        resultsList.innerHTML = "<li>Please enter a class!<li/>"
        return;
    }

    fetch(`/search?q=${query}`)
        .then(response => response.json())
        .then(data => {
            console.log("JSON Response:", data);


            if(data.error) {
                resultsList.innerHTML = `<li>${data.error}</li>`;
                return;
            }
            data.forEach(item => {
                const li = document.createElement("li");
                li.textContent = `${item.title} - $${item.category}`;
                resultsList.appendChild(li);
            });

            if (data.length === 0) {
                resultsList.innerHTML = "<li>No products found</li>";
                return;
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
}