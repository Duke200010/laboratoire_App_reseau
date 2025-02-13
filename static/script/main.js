$(document).ready(function() {
    $('#horoscopeForm').submit(function(event) {
        event.preventDefault(); 

        
        $.ajax({
            url: '/horoscope', 
            type: 'POST',      
            data: $(this).serialize(), 
            success: function(response) {
                
                if (response.erreur) {
                    $('#horoscope').html('<p style="color:red;">' + response.erreur + '</p>');
                } else {
                    $('#horoscope').html(
                        '<p>Bonjour ' + response.prenom + ' ' + response.nom + '!</p>' +
                        '<p>Votre signe du zodiaque est : ' + response.signe + '</p>' +
                        '<p>Prédiction : ' + response.prediction + '</p>' +
                        '<img src="/static/images/' + response.image + '" alt="' + response.signe + '">'                    );
                }
            },
            error: function() {
                
                $('#horoscope').html('<p style="color:red;">Une erreur s\'est produite.</p>');
            }
        });
    });
});