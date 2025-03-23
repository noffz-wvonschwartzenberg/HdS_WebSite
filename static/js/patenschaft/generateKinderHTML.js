import {kinder} from './kinder.js';

export function generateKinderHTML(showkinderOhnePaten, showButton, linkedPage)
{
    let kinderOhnePatenHTML = '';

    kinder.forEach((kind) => {
        if (kind.HabenEinenPaten !== showkinderOhnePaten && showkinderOhnePaten && !linkedPage)
        {
            const containerHTML = `<div id="profile-container-${kind.id}" class="profile-container">`;
            const geborenHTML = `geboren ${kind.Geburtsdatum}` + (kind.Geburtsort != '' ? ` in ${kind.Geburtsort}` : ``);
            const buttonHTML = (showButton === true ? `<button onclick=
                "
                const container = document.getElementById('profile-container-${kind.id}');
                const button = this;
                if (container.classList.contains('profile-container-selected'))
                {
                    container.classList.remove('profile-container-selected');
                    button.textContent = 'Auswählen';
                } else {
                    container.classList.add('profile-container-selected');
                    button.textContent = 'Ausgewählt';
                }
                "
                >Auswählen</button>` : ``);
                
            kinderOhnePatenHTML += `
            ${containerHTML}
                <img src="${kind.Bild}">
                <div>
                    <p>${kind.Name}</p>
                    <p>${geborenHTML} </p>  
                    <p>${kind.KurzeBeschreibung}</p>
                </div>
                ${buttonHTML}
            </div>`;
        }

        if (kind.HabenEinenPaten !== showkinderOhnePaten && showkinderOhnePaten && linkedPage)
        {
            const containerHTML = `<div id="profile-container-${kind.id}" class="profile-container">`;
            const geborenHTML = `geboren ${kind.Geburtsdatum}` + (kind.Geburtsort != '' ? ` in ${kind.Geburtsort}` : ``);
            const buttonHTML = (showButton === true ? `<button onclick=
                "
                window.location.href = '../../Helfen/pateWerden';
                "
                >Patenschaft übernehmen</button>` : ``);
                
            kinderOhnePatenHTML += `
            ${containerHTML}
                <img src="${kind.Bild}">
                <div>
                    <p>${kind.Name}</p>
                    <p>${geborenHTML} </p>  
                    <p>${kind.KurzeBeschreibung}</p>
                </div>
                ${buttonHTML}
            </div>`;
        }
            
        if (kind.HabenEinenPaten !== showkinderOhnePaten && !showkinderOhnePaten)
        {
            const containerHTML = `<div class="profile-container profile-container-supplied">`;
            const geborenHTML = `geboren ${kind.Geburtsdatum}` + (kind.Geburtsort != '' ? ` in ${kind.Geburtsort}` : ``);
            
            kinderOhnePatenHTML += `
            ${containerHTML}
                <img src="${kind.Bild}">
                <div>
                    <p>${kind.Name}</p>
                    <p>${geborenHTML} </p>  
                    <p>${kind.KurzeBeschreibung}</p>
                </div>
            </div>`;
        }
    });

    return kinderOhnePatenHTML;
}

