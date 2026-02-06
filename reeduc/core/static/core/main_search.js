document.addEventListener('DOMContentLoaded', () => {
    const searchBoxes = document.querySelectorAll('.search');
    if (!searchBoxes.length) return;

    const buildResults = (container) => {
        const results = document.createElement('div');
        results.className = 'search-results';
        results.style.display = 'none';
        container.appendChild(results);
        return results;
    };

    const fetchResults = async (query) => {
        const response = await fetch(`/agendamentos/buscar?q=${encodeURIComponent(query)}`);
        if (!response.ok) return [];
        const data = await response.json();
        return data.results || [];
    };

    searchBoxes.forEach((box, index) => {
        const input = box.querySelector('input');
        if (!input) return;
        if (!input.id) {
            input.id = index === 0 ? 'mainSearch' : `mainSearch-${index}`;
        }
        input.setAttribute('autocomplete', 'off');

        const results = buildResults(box);
        let currentItems = [];

        const closeResults = () => {
            results.style.display = 'none';
            results.innerHTML = '';
            currentItems = [];
        };

        input.addEventListener('input', async () => {
            const query = input.value.trim();
            if (query.length < 2) {
                closeResults();
                return;
            }

            const items = await fetchResults(query);
            currentItems = items;
            results.innerHTML = '';

            if (!items.length) {
                closeResults();
                return;
            }

            items.forEach((item) => {
                const row = document.createElement('div');
                row.className = 'search-result-item';
                row.textContent = item.text;
                row.addEventListener('click', () => {
                    window.location.href = `/cadastro/perfil/${item.id}`;
                });
                results.appendChild(row);
            });
            results.style.display = 'block';
        });

        document.addEventListener('click', (event) => {
            if (!box.contains(event.target)) {
                closeResults();
            }
        });
    });
});
