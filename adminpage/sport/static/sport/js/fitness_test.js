let students_in_table = {};
let exercises = [];

fetch('/api/fitnesstest/sessions', {
	method: 'GET',
	'X-CSRFToken': csrf_token,
})
	.then((response) => {
		return response.json();
	})
	.then((data) => {
		data.forEach((session) => {
			let d = new Date(session.date);
			let mon = d.toLocaleString('en-US', { month: 'short' });
			let session_row = $(
				// Temporary solution, before was with the django url:
				`<tr style="cursor: pointer" onclick="location.href='${
					session.id
				}'">
                    <td scope="row">
                        <span>
                        Session at <i>${d.getHours()}:${d.getMinutes()}, ${mon} ${d.getDate()}, ${d.getFullYear()}</i>
                        </span>
                    </td>
                    <td>
                        <span class="badge badge-pill badge-light">${
							session.teacher
						}</span>
                    </td>
                </tr>`
			);
			$('#ft-session-table-body').prepend(session_row);
		});
	})
	.catch(function (err) {
		console.log(err);
	});
