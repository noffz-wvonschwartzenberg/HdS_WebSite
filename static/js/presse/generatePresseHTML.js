import {presse} from './presse.js';

export function generatePresseHTML()
{
    let presseHTML = '';
    presse.forEach((press) => {
        if(press.ArticlePdf === "") {
            presseHTML += `
            <div class="article-line" onclick="window.location.href='${press.ArticleLink}'">
                <div class="article-column">
                    <img src="${press.Logo}" alt="${press.LogoText}" class="image-logo">
                    <p class="article-date">${press.ArticleDate}</p>
                </div>
                <a class="article-title">${press.ArticleTitle}</a>
            </div>`;
        } else {
            presseHTML += `
            <details style="margin 10px;">
                <summary class="combobox-summary">
                    <p></p>
                    <img src="${press.Logo}" alt="${press.LogoText}" class="image-logo" style="width: auto; max-width: 100px; height: auto; max-height: 35px;">
                    <p class="article-date" style="font-size: 12px;">Date: ${press.ArticleDate}</p>
                    ${press.ArticleTitle}
                </summary>
                <div class="combobox-details">  
                    <iframe src="${press.ArticlePdf}" title="${press.ArticleTitle}" width="100%">
                    Ihr Browser unterstützt keine PDF-Anzeige.
                    </iframe>
                </div>
            </details>`;
        }
    });

    return presseHTML;
}

