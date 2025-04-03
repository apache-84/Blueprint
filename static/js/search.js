function searchItems() {
    event.preventDefault();

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
                li.innerHTML = `<a href="${item.class}">${item.name}</a>`;
                resultsList.appendChild(li);
            });

            if (data.length === 0) {
                resultsList.innerHTML = "<li>No class found</li>";
                return;
            }
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
}