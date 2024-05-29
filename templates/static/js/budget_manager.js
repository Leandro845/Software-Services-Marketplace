// Dados de exemplo (substitua por dados reais do Django)
const softwereMakerData = [
    // ... seus dados aqui
];

// ... (dados de exemplo para expenseManagementMakerData e groupRevenueMakerData)

// Função para carregar dados na tabela
function loadData(data, tableBodyId) {
    const tableBody = document.getElementById(tableBodyId);
    tableBody.innerHTML = ''; // Limpa a tabela

    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.project_description}</td>
            <td>${item.project_requirements}</td>
            <td>${item.project_duration}</td>
            <td>${item.project_complexity}</td>
            <td>${item.name_surname}</td>
            <td>${item.phone_number}</td>
            <td>${item.email_client}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Função para buscar dados filtrados do servidor (apenas se necessário)
// ... (implementação da função fetchFilteredData, se aplicável)

// Event Listener para a barra de pesquisa
const searchBar = document.querySelector('.search-bar input');
searchBar.addEventListener('input', () => {
    const searchTerm = searchBar.value.toLowerCase();
    const filteredData = softwereMakerData.filter(item => {
        return Object.values(item).some(value =>
            String(value).toLowerCase().includes(searchTerm)
        );
    });
    loadData(filteredData, 'softweremaker-table-body');
    loadPage(1, 'softweremaker'); // Reinicia a paginação após a pesquisa
});

// Funcionalidade de paginação
const paginationButtons = document.querySelectorAll('.pagination button');
const itemsPerPage = 5;
let currentPage = 1;

function updatePagination(section) {
    const data = dataBySection[section];
    const totalPages = Math.ceil(data.length / itemsPerPage);

    const pagination = document.querySelector(`.pagination[data-section="${section}"]`);
    pagination.querySelector('.prev').disabled = currentPage === 1;
    pagination.querySelector('.next').disabled = currentPage === totalPages;
}

function loadPage(page, section) {
    currentPage = page;
    const data = dataBySection[section];
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const paginatedData = data.slice(startIndex, endIndex);
    const tableBodyId = `${section}-table-body`;
    loadData(paginatedData, tableBodyId);
    updatePagination(section);
}

paginationButtons.forEach(button => {
    const section = button.closest('.pagination').dataset.section;
    button.addEventListener('click', () => {
        if (button.classList.contains('prev')) {
            loadPage(currentPage - 1, section);
        } else if (button.classList.contains('next')) {
            loadPage(currentPage + 1, section);
        }
    });
});

// Inicialização
const dataBySection = {
    'softweremaker': softwereMakerData,
    // ... (adicione outras seções, se houver)
};
loadPage(1, 'softweremaker');