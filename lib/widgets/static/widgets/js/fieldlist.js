$(document).ready(function() {
    $('body').on('click', '.btn-del-fieldlist', function() {
        var fieldlist = $(this).parentsUntil('.fieldlist').parent(),
            selected = $(this).parentsUntil('.fieldlist-item').parent(),
            items = fieldlist.find('.fieldlist-item');

        if (items.length > 1) {
            selected.remove();
        } else {
            selected.find('input').each(function() {
                $(this).val('');
            });
        }
    });

    $('body').on('click', '.btn-add-fieldlist', function() {
        var fieldlist = $(this).parentsUntil('.fieldlist').parent(),
            selected = fieldlist.find('.fieldlist-item:last-child').clone(),
            target = fieldlist.find('.fieldlist-item:last-child').parent(),
            sid = selected.find('input:text:first').attr('id'),
            nid = Number(sid.split("-")[1]);

        selected.appendTo(target);
        selected.find('input').each(function() {
            $(this).attr('id', $(this).attr('id').replace(nid, nid+1));
            $(this).attr('name', $(this).attr('name').replace(nid, nid+1));
            $(this).val('');
        })

    });
});