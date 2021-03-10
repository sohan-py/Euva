function indexScroll() {
    const featuresTop = document.getElementById('features').offsetTop;
    const navHome = document.getElementById('nav-home');
    const navFeatures = document.getElementById('nav-features');
    if (window.scrollY >= featuresTop - 100) {
        navHome.classList.remove('active');
        navHome.classList.remove('index-nav-active');
        navFeatures.classList.add('active');
        navFeatures.classList.add('index-nav-active');
    } else {
        navHome.classList.add('active');
        navHome.classList.add('index-nav-active');
        navFeatures.classList.remove('active');
        navFeatures.classList.remove('index-nav-active');
    }
}

function dragElement(element) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    document.getElementById(element.id + '-header').onmousedown = dragMouseDown;

    function dragMouseDown(event) {
        pos3 = event.clientX;
        pos4 = event.clientY;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(event) {
        pos1 = pos3 - event.clientX;
        pos2 = pos4 - event.clientY;
        pos3 = event.clientX;
        pos4 = event.clientY;
        element.style.top = (element.offsetTop - pos2) + 'px';
        element.style.left = (element.offsetLeft - pos1) + 'px';
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

function getDateString(date) {
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    date = date.split('-');
    return monthNames[parseInt(date[1]) - 1] + ' ' + date[2] + ', ' + date[0]
}

dragElement(document.getElementById('chatbox'));
