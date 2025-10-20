
   document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM loaded - modal script running');

    const modal = document.getElementById('orderModal');
    const openBtns = document.querySelectorAll('.open-order-modal');
    const closeBtn = document.querySelector('.close-modal');

    // Проверка элементов
    if (!modal) {
        console.error('Modal element not found');
        return;
    }
    if (openBtns.length === 0) {
        console.error('Open buttons not found');
        return;
    }
    if (!closeBtn) {
        console.error('Close button not found');
    }

    console.log(`Found ${openBtns.length} open buttons`);

    // Открыть модалку
    openBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const flowerId = this.dataset.flowerId;
            const flowerName = this.dataset.flowerName;

            document.getElementById('flower-id-field').value = flowerId;
            document.getElementById('flower-name-display').textContent = flowerName;

            console.log('Open button clicked');
            modal.style.display = 'block';
        });
    });

    // Закрыть по крестику
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            console.log('Close button clicked');
            modal.style.display = 'none';
        });
    }

    // Закрыть при клике вне формы
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            console.log('Background clicked');
            modal.style.display = 'none';
        }
    });
});
