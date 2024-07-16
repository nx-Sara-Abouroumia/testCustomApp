
frappe.listview_settings['Quotation'] = {
    formatters: {
        status: function(value, doc) {
            if (value === 'Open') {
                return `<span class="label label-warning">${__('Open')}</span> <span class="label label-info">${__('Submitted')}</span>`;
            }
            return value;
        }
    }
};
