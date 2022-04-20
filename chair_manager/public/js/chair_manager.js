// Copyright (c) 2017, Frappé and contributors
// For license information, please see license.txt

var console_dialog = (key) => {
	var dialog = new vmraid.ui.Dialog({
		title: 'Console',
		fields: [
			{fieldname: 'console', fieldtype: 'HTML'},
		]
	});
	vmraid._output_target = $('<pre class="console"><code></code></pre>')
		.appendTo(dialog.get_field('console').wrapper)
		.find('code')
		.get(0);
	vmraid._output = '';
	vmraid._in_progress = false;
	vmraid._output_target.innerHTML = '';
	dialog.show();
	dialog.$wrapper.find('.modal-dialog').css('width', '800px');

	vmraid.realtime.on(key, function(output) {
		if (output==='\r') {
			// clear current line, means we are showing some kind of progress indicator
			vmraid._in_progress = true;
			if(vmraid._output_target.innerHTML != vmraid._output) {
				// progress updated... redraw
				vmraid._output_target.innerHTML = vmraid._output;
			}
			vmraid._output = vmraid._output.split('\n').slice(0, -1).join('\n') + '\n';
			return;
		} else {
			vmraid._output += output;
		}

		if (output==='\n') {
			vmraid._in_progress = false;
		}

		if (vmraid._in_progress) {
			return;
		}

		if (!vmraid._last_update) {
			vmraid._last_update = setTimeout(() => {
				vmraid._last_update = null;
				if(!vmraid.in_progress) {
					vmraid._output_target.innerHTML = vmraid._output;
				}
			}, 200);
		}
	});
};