// Initialize charts
document.addEventListener('DOMContentLoaded', function() {
    // Animate coverage progress
    setTimeout(function() {
        document.getElementById('coverageProgress').style.width = '90%';
    }, 500);
    
    // Savings Chart
    const savingsCtx = document.getElementById('savingsChart').getContext('2d');
    const savingsChart = new Chart(savingsCtx, {
        type: 'doughnut',
        data: {
            labels: ['Saved', 'Remaining'],
            datasets: [{
                data: [65, 35],
                backgroundColor: [
                    'rgba(109, 179, 63, 0.8)',
                    'rgba(241, 241, 241, 0.8)'
                ],
                borderColor: [
                    'rgb(109, 179, 63)',
                    'rgb(241, 241, 241)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.raw + '%';
                        }
                    }
                }
            }
        }
    });
    
    // Investment Chart
    const investmentCtx = document.getElementById('investmentChart').getContext('2d');
    const investmentChart = new Chart(investmentCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Portfolio Value',
                data: [18000, 19500, 21000, 22400, 23100, 24180],
                borderColor: 'rgb(12, 75, 51)',
                backgroundColor: 'rgba(12, 75, 51, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return 'R ' + context.raw.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        callback: function(value) {
                            return 'R ' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
    
    // Business Chart
    const businessCtx = document.getElementById('businessChart').getContext('2d');
    const businessChart = new Chart(businessCtx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar'],
            datasets: [{
                label: 'Business Income',
                data: [7800, 9200, 12500],
                backgroundColor: 'rgba(249, 202, 36, 0.8)',
                borderColor: 'rgb(249, 202, 36)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return 'R ' + context.raw.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return 'R ' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
    
    // Travel Chart
    const travelCtx = document.getElementById('travelChart').getContext('2d');
    const travelChart = new Chart(travelCtx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar'],
            datasets: [{
                label: 'Travel Savings',
                data: [980, 1240, 1620],
                backgroundColor: 'rgba(127, 140, 141, 0.8)',
                borderColor: 'rgb(127, 140, 141)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return 'R ' + context.raw.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return 'R ' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
    
    // Task checkbox functionality
    const checkboxes = document.querySelectorAll('.task-checkbox');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('click', function() {
            this.classList.toggle('checked');
            this.innerHTML = this.classList.contains('checked') ? '✓' : '';
        });
    });
    
    // Tab functionality
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            this.classList.add('active');
        });
    });

    // AI Assist Button Functionality
    const aiAssistButton = document.getElementById('aiAssistButton');
    const aiAssistChat = document.getElementById('aiAssistChat');
    const closeChat = document.getElementById('closeChat');
    
    aiAssistButton.addEventListener('click', function() {
        aiAssistChat.classList.toggle('active');
    });
    
    closeChat.addEventListener('click', function() {
        aiAssistChat.classList.remove('active');
    });
});