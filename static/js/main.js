const searchInput = document.getElementById('search-input');
const resultsList = document.getElementById('results');
const termDetail = document.getElementById('term-detail');
const detailTitle = document.getElementById('detail-title');
const detailCategory = document.getElementById('detail-category');
const detailDefinition = document.getElementById('detail-definition');

searchInput.addEventListener('input', async (e) => {
    const query = e.target.value;
    if (query.length < 2) {
        resultsList.innerHTML = '';
        return;
    }

    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        
        displayResults(results);
    } catch (error) {
        console.error('Search error:', error);
    }
});

function displayResults(results) {
    resultsList.innerHTML = '';
    results.forEach(item => {
        const div = document.createElement('div');
        div.className = 'result-item';
        div.textContent = item.term;
        div.onclick = () => showDetail(item);
        resultsList.appendChild(div);
    });
}

function showDetail(item) {
    detailTitle.textContent = item.term;
    detailCategory.textContent = item.category || '기타';
    detailDefinition.textContent = item.definition;
    termDetail.classList.remove('hidden');
    resultsList.innerHTML = '';
    searchInput.value = '';
}

function closeDetail() {
    termDetail.classList.add('hidden');
}
