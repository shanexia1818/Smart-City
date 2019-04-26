const db = firebase.firestore();
db.settings({ timestampsInSnapshots: true });

db.collection('garbage_1').get().then((snapshot) => {
	snapshot.docs.forEach(doc => {
		let house_info = document.getElementbyClass("house_info");
		house_info.innerHTML += `
			<div class="card-panel z-depth-0 house-info">
                <span>${doc.data()}</span>
            </div>
		`;
	})
});
