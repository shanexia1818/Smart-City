const db = firebase.firestore();
db.settings({ timestampsInSnapshots: true });

db.collection('garbage_1').onSnapshot((snapshot) => {
	snapshot.docChanges().forEach(doc => {
		let house_info = document.getElementbyClassName(".house_info");
		house_info.innerHTML += `
			<div class="card-panel z-depth-0">
                <span>${doc.data()}</span>
            </div>
		`;
	})
});
