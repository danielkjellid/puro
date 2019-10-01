/* Notes */ 
const showMoreNotesBtn = $('button.show-more-notes');
const notesContainer = $('div.notes-container');
const normalNotes = $('div.normal-note');
const notesContainerNormalNote = $('div.notes-container').find('div.normal-note');
const addNoteBtn = $('button.add-note-btn');
const addNoteField = $('div.add-note-field');
const addNoteCancelBtn = $('button.add-note-cancel-btn');
const showMoreNotes = $('div.show-more-notes-container');

//Adds class hidden when amount of normal notes is above 2 in total
notesContainerNormalNote.slice(2, normalNotes.length).addClass('hidden');
console.log(normalNotes.length)

if (normalNotes.length <= 2) {
    showMoreNotes.addClass('hidden');
}

//Eventlistener for showing the hidden notes when the amount of normal notes is above 2
showMoreNotesBtn.on('click', function() {
    notesContainerNormalNote.slice(2, normalNotes.length).removeClass('hidden');
});

//Eventlistener for showing the add note field on button blick
addNoteBtn.on('click', function(){
    addNoteField.removeClass('hidden');
});

//Eventlistener for hiding the add note field on button blick
addNoteCancelBtn.on('click', function() {
    addNoteField.addClass('hidden');
});



