const softwareMakerBudgetForm = document.getElementById('software-maker-budget-form');

softwareMakerBudgetForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const projectName = document.getElementById('project-name').value;
    const projectDescription = document.getElementById('project-description').value;
    const projectRequirements = document.getElementById('project-requirements').value;
    const projectDuration = document.getElementById('project-duration').value;
    const projectComplexity = document.getElementById('project-complexity').value;

    // Send the budget request to the server using AJAX or other methods
    console.log('
