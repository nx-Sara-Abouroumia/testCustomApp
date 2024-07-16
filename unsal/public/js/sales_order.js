frappe.ui.form.on('Sales Order', {
    before_save: function(frm) {
        let threeMonthsAhead = frappe.datetime.add_months(frappe.datetime.now_date(), 3);

        frm.doc.items.forEach(function(item) {
            if (!item.delivery_date) {
                item.delivery_date = threeMonthsAhead;
            }
        });
    },


    before_load: function(frm) {
        // Hide the delivery_date column in the items table
        var df =frappe.meta.get_docfield('Sales Order Item', 'delivery_date',frm.doc.name);
        df.hidden=1;
        frm.refresh_fields();
    }

});