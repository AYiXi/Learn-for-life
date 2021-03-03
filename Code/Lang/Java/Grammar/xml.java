// java 处理 xml
// java 处理 xpath
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;

// 解析 xml 获取 entid, companName, credit_ticket
private static List<HashMap<String, String>> analyzeEntIdXml(String html) {
    List<HashMap<String, String>> list = new ArrayList<>();
    String entid = null;
    String companyName = null;
    String creditTicket = null;
    try {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = factory.newDocumentBuilder();
        Document document = documentBuilder.parse(new InputSource(new StringReader(html)));
        Element root = document.getDocumentElement();
        NodeList nodeList = root.getChildNodes();

        if (nodeList != null) {
            for (int i = 0; i < nodeList.getLength(); i++) {
                Node node = nodeList.item(i);
                if (node.getNodeType() == Node.ELEMENT_NODE) {
                    // 避免出现对应错误的情况
                    entid = null;
                    companyName = null;
                    creditTicket = null;

                    for (Node node1 = node.getFirstChild(); node1 != null; node1 = node1.getNextSibling()) {
                        if (node1.getNodeType() == Node.ELEMENT_NODE) {
                            if (node1.getNodeName().equals("entid")) {
                                entid = node1.getFirstChild().getNodeValue();
                                System.out.println("entid = " + entid);
                            }

                            if (node1.getNodeName().equals("ent_name")) {
                                companyName = node1.getFirstChild().getNodeValue();
                                System.out.println("companyName = " + companyName);
                            }

                            if (node1.getNodeName().equals("credit_ticket")) {
                                creditTicket = node1.getFirstChild().getNodeValue();
                                System.out.println("credit_ticket = " + creditTicket);
                            }

                            if (entid != null && companyName != null && creditTicket != null) {
                                break;
                            }
                        }
                    }

                    // 确保三个参数是对应的并且是同时生成的
                    if (entid != null && companyName != null && creditTicket != null) {
                        HashMap<String, String> s = new HashMap<>();
                        s.put("entid", entid);
                        s.put("companyName", companyName);
                        s.put("creditTicket", creditTicket);
                        list.add(s);
                    }
                }
            }
        }

    } catch (Exception e) {
        println("error html:" + html);
        e.printStackTrace();
    }

    return list;
}

// 解析 xml 获取开业状态
private static String analyzeStatusXml(String html) {
    String status = null;

    try {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = factory.newDocumentBuilder();
        Document document = documentBuilder.parse(new InputSource(new StringReader(html)));

        XPathFactory xPathFactory = XPathFactory.newInstance();
        XPath xPath = xPathFactory.newXPath();

        Node node = (Node) xPath.evaluate("qyxx/jcxx/gsdjxx/ent_state", document, XPathConstants.NODE);
        // 经营状态@_@注销
        status = node.getFirstChild().getNodeValue();

        if (status.contains("吊销") || status.contains("注销")) {
            status = "注销";
        } else {
            status = "开业";
        }

    } catch (Exception e) {
        e.printStackTrace();
    }

    return status;
}