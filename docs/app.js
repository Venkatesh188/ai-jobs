document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('jobsContainer');
    const searchInput = document.getElementById('searchInput');
    const statsDiv = document.getElementById('jobStats');
    
    let allJobs = [];

    // Fetch jobs data
    fetch('jobs.json')
        .then(response => response.json())
        .then(data => {
            allJobs = data;
            renderJobs(allJobs);
            updateStats(allJobs.length);
        })
        .catch(error => {
            console.error('Error loading jobs:', error);
            container.innerHTML = '<p style="text-align:center; color: red;">Error loading job data. Please try again later.</p>';
        });

    // Search functionality
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const filtered = allJobs.filter(job => 
            (job.title && job.title.toLowerCase().includes(term)) ||
            (job.company && job.company.toLowerCase().includes(term)) ||
            (job.location && job.location.toLowerCase().includes(term))
        );
        renderJobs(filtered);
        updateStats(filtered.length);
    });

    function updateStats(count) {
        statsDiv.textContent = `${count} jobs found`;
    }

    function renderJobs(jobs) {
        container.innerHTML = '';
        
        if (jobs.length === 0) {
            container.innerHTML = '<p style="grid-column: 1/-1; text-align: center;">No jobs found matching your criteria.</p>';
            return;
        }

        jobs.forEach(job => {
            const card = document.createElement('div');
            card.className = 'job-card';
            
            // Handle missing data gracefully
            const title = job.title || 'Untitled Role';
            const company = job.company || 'Unknown Company';
            const location = job.location || 'Remote / Unspecified';
            const url = job.url || '#';
            const date = job.date || 'Recently';

            card.innerHTML = `
                <h3 class="job-title">${escapeHtml(title)}</h3>
                <div class="job-company">${escapeHtml(company)}</div>
                <div class="job-meta">
                    <span>📍 ${escapeHtml(location)}</span>
                    <span>📅 ${escapeHtml(date)}</span>
                </div>
                <a href="${url}" target="_blank" class="btn">Apply Now</a>
            `;
            
            container.appendChild(card);
        });
    }

    function escapeHtml(text) {
        if (!text) return '';
        return text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
});
