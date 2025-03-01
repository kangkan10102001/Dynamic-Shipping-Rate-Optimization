document.getElementById("predictionForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    let weight = document.getElementById("weight").value;
    let distance = document.getElementById("distance").value;

    let response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ weight: weight, distance: distance })
    });

    let data = await response.json();
    document.getElementById("result").innerText = data.shipping_rate ? `$${data.shipping_rate}` : "Error";
});
