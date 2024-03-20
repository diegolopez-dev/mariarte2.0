// Envió de formulario

const $form = document.getElementById('form');

$form.addEventListener('submit', handleSubmit);

async function handleSubmit(event) {
	event.preventDefault()
	const form = new FormData(this)
	const response = await fetch(this.action, {
		method: this.method,
		body: form, 
		headers: {
			'Accept': 'application/json'
		}
	})
	if (response.ok) {
		this.reset()
		Swal.fire({
			title: "¡GRACIAS!",
			text: "Correo enviado correctamente",
			iconColor: '#faffbe',
			color: '#faffbe',
			background: '#141212',
			icon: "success"
		  });
	}
	else {
		this.reset()
		Swal.fire({
			icon: "error",
			title: "¡ERROR!",
			text: "Revisa los datos",
			iconColor: '#faffbe',
			color: '#faffbe',
			background: '#141212'
		  });
	}
}