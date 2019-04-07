/*
 * Materialise specific script for dropdown menu on mobile screens.
 */
document.addEventListener('DOMContentLoaded', () => {
    let elems = document.querySelectorAll('.sidenav');
    let instances = M.Sidenav.init(elems, options);
});