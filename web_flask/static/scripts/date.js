document.addEventListener("DOMContentLoaded", function () {
    function updateDate () {
        const dateContainer = document.getElementById('day');
        const date = new Date();
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const formattedDate = date.toLocaleDateString(undefined, options);
        dateContainer.innerHTML = `<p>${formattedDate}</p>`
    }

    updateDate();
})