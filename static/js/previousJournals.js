let previousJournalChart;
const previousJournalctx = document.getElementById('previous-journal-ctx');

function downloadJournal() {
    let text = '';
    for (i = 0; i < currPreviousJournalBlocks.length; i++) { text += currPreviousJournalBlocks[i].data.text + '\n\n'; }
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', 'EuvaJournal ' + journalDate);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

function graphPreviousJournal(sentimentScore) {
    const previousJournalData = {
        labels: ['Positive Sentiment', 'Negative Sentiment'],
        datasets: [{
            label: 'Sentimental Analysis',
            data: [sentimentScore, (100 - sentimentScore).toFixed(2)],
            backgroundColor: ['rgba(69, 204, 88, 0.5)', 'rgba(220, 53, 69, 0.5)'],
            borderColor: ['rgba(69, 204, 88, 1)', 'rgba(220, 53, 69, 1)'],
            borderWidth: 1,
            fill: true
        }]
    };
    if (previousJournalChart != undefined) { previousJournalChart.destroy(); }
    previousJournalChart = new Chart(previousJournalctx, {
        type: 'doughnut',
        data: previousJournalData
    });
}
