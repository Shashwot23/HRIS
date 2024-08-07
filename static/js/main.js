

var ctxHeadcount = document.getElementById('headcountChart').getContext('2d');
var headcountChart = new Chart(ctxHeadcount, {
    type: 'bar',
    data: {
        labels: departmentNames,
        datasets: [{
            label: 'Employee Headcount',
            data: headcounts,
            backgroundColor: ['#007bff', '#28a745', '#dc3545', '#ffc107', '#17a2b8']
        }]
    }
});

var ctxTurnover = document.getElementById('turnoverChart').getContext('2d');
var turnoverChart = new Chart(ctxTurnover, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        datasets: [{
            label: 'Turnover Rate',
            data: [3, 4, 5, 2, 3],
            borderColor: '#dc3545',
            fill: false
        }]
    }
});

